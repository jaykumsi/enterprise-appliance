# How to run (GCP IAM version of your AWS IAM policies)
# 1. Go to the folder you want to execute the run
# 2. terraform init
# 3. terraform plan
# 4. terraform apply
#
# Notes:
# - GCP doesn't have AWS-style "IAM Policies" JSON attached to users/groups; it uses IAM roles on a scope.
# - This file creates Google Cloud Storage buckets (S3 equivalent), a BigQuery dataset (Athena equivalent),
#   and Service Accounts to represent your "Groups" (devopsadmin/instructor/developer/etc).
# - If you want to use actual Google Groups instead of Service Accounts, you typically need
#   Cloud Identity / Google Workspace + additional Terraform/provider setup.
#
# Mapping (roughly):
# - AWS devopsadmin (ec2/s3/rds/iam/...)     -> GCP Project "Owner" (broad) or "Editor" (less broad)
# - AWS S3 bucket policies                   -> GCS bucket IAM roles
# - AWS Glue                                 -> GCP Dataflow roles (as an ETL/orchestration analogue)
# - AWS Athena read-only                      -> BigQuery dataset Data Viewer + Job User
# - AWS Lambda user/policy                    -> Cloud Functions Developer
#
# You can copy this into a main.tf and adjust variables as needed.

terraform {
  required_version = ">= 1.5.0"

  required_providers {
    google = {
      source  = "hashicorp/google"
      version = ">= 5.20.0"
    }
    random = {
      source  = "hashicorp/random"
      version = ">= 3.6.0"
    }
  }
}

# ----------------------------
# Provider
# ----------------------------
provider "google" {
  project = var.project_id
  region  = var.region

  # Auth options:
  # 1) Application Default Credentials (recommended for local):
  #    gcloud auth application-default login
  #
  # 2) Service account JSON key:
  #    export GOOGLE_APPLICATION_CREDENTIALS="/path/key.json"
}

# ----------------------------
# Variables
# ----------------------------
variable "project_id" {
  type        = string
  description = "GCP Project ID"
}

variable "region" {
  type        = string
  default     = "us-central1"
  description = "Default region"
}

variable "location" {
  type        = string
  default     = "US"
  description = "BigQuery dataset location"
}

# ----------------------------
# Random suffix (bucket names must be globally unique)
# ----------------------------
resource "random_string" "suffix" {
  length  = 6
  upper   = false
  lower   = true
  numeric = true
  special = false
}

# ----------------------------
# Storage (S3 analogue) -> GCS Buckets
# ----------------------------
resource "google_storage_bucket" "students_bucket" {
  name                        = "ti-p-students-${random_string.suffix.result}"
  location                    = var.region
  uniform_bucket_level_access = true

  public_access_prevention = "enforced"

  versioning {
    enabled = true
  }
}

resource "google_storage_bucket" "etl_bucket" {
  name                        = "ti-p-etl-data-${random_string.suffix.result}"
  location                    = var.region
  uniform_bucket_level_access = true
  public_access_prevention    = "enforced"
}

resource "google_storage_bucket" "instructor_bucket" {
  name                        = "ti-p-instructor-${random_string.suffix.result}"
  location                    = var.region
  uniform_bucket_level_access = true
  public_access_prevention    = "enforced"
}

# ----------------------------
# BigQuery (Athena analogue) -> BigQuery Dataset
# ----------------------------
resource "google_bigquery_dataset" "analytics_ds" {
  dataset_id  = "ti_analytics"
  location    = var.location
  description = "Analytics dataset (Athena read-only analogue)"
}

# ----------------------------
# Service Accounts (used here as "group-like" principals)
# ----------------------------
resource "google_service_account" "ti_devopsadmin" {
  account_id   = "ti-devopsadmin"
  display_name = "ti-devopsadmin (broad admin SA)"
}

resource "google_service_account" "ti_instructor_storage" {
  account_id   = "ti-instructor-storage"
  display_name = "ti instructor storage SA"
}

resource "google_service_account" "ti_developer_storage" {
  account_id   = "ti-developer-storage"
  display_name = "ti developer storage SA"
}

resource "google_service_account" "ti_instructor_etl" {
  account_id   = "ti-instructor-etl"
  display_name = "ti instructor ETL SA"
}

resource "google_service_account" "ti_developer_etl" {
  account_id   = "ti-developer-etl"
  display_name = "ti developer ETL SA"
}

resource "google_service_account" "ti_analytics_readonly" {
  account_id   = "ti-analytics-readonly"
  display_name = "ti analytics read-only SA"
}

resource "google_service_account" "ti_viz_readonly" {
  account_id   = "ti-viz-readonly"
  display_name = "ti visualization read-only SA"
}

resource "google_service_account" "ti_viz_readwrite" {
  account_id   = "ti-viz-readwrite"
  display_name = "ti visualization read-write SA"
}

resource "google_service_account" "lambda_user" {
  account_id   = "lambda-user"
  display_name = "lambda-user (Cloud Functions SA)"
}

# ----------------------------
# IAM bindings (equivalent of attaching AWS IAM policies)
# ----------------------------

# 1) DevOps Admin (broad admin) -> Project Owner
resource "google_project_iam_member" "ti_devopsadmin_owner" {
  project = var.project_id
  role    = "roles/owner"
  member  = "serviceAccount:${google_service_account.ti_devopsadmin.email}"
}

# 2) Instructor Storage: Get/Put/Delete/List on instructor bucket
#    - objectAdmin => create/read/update/delete objects
#    - legacyBucketReader => list bucket (and some bucket read)
resource "google_storage_bucket_iam_member" "instructor_bucket_object_admin" {
  bucket = google_storage_bucket.instructor_bucket.name
  role   = "roles/storage.objectAdmin"
  member = "serviceAccount:${google_service_account.ti_instructor_storage.email}"
}

resource "google_storage_bucket_iam_member" "instructor_bucket_list" {
  bucket = google_storage_bucket.instructor_bucket.name
  role   = "roles/storage.legacyBucketReader"
  member = "serviceAccount:${google_service_account.ti_instructor_storage.email}"
}

# 3) ETL Developer Storage: Get/Put/List on ETL bucket (no delete)
resource "google_storage_bucket_iam_member" "etl_bucket_object_creator" {
  bucket = google_storage_bucket.etl_bucket.name
  role   = "roles/storage.objectCreator"
  member = "serviceAccount:${google_service_account.ti_developer_storage.email}"
}

resource "google_storage_bucket_iam_member" "etl_bucket_object_viewer" {
  bucket = google_storage_bucket.etl_bucket.name
  role   = "roles/storage.objectViewer"
  member = "serviceAccount:${google_service_account.ti_developer_storage.email}"
}

resource "google_storage_bucket_iam_member" "etl_bucket_list" {
  bucket = google_storage_bucket.etl_bucket.name
  role   = "roles/storage.legacyBucketReader"
  member = "serviceAccount:${google_service_account.ti_developer_storage.email}"
}

# 4) Instructor ETL (Glue:*) analogue -> Dataflow Admin (project level)
resource "google_project_iam_member" "instructor_dataflow_admin" {
  project = var.project_id
  role    = "roles/dataflow.admin"
  member  = "serviceAccount:${google_service_account.ti_instructor_etl.email}"
}

# 5) ETL Developer (limited) -> Dataflow Viewer
resource "google_project_iam_member" "developer_dataflow_viewer" {
  project = var.project_id
  role    = "roles/dataflow.viewer"
  member  = "serviceAccount:${google_service_account.ti_developer_etl.email}"
}

# 6) Analytics read-only (Athena read-only analogue) -> BigQuery dataset Data Viewer + Job User
resource "google_bigquery_dataset_iam_member" "analytics_ds_data_viewer" {
  dataset_id = google_bigquery_dataset.analytics_ds.dataset_id
  role       = "roles/bigquery.dataViewer"
  member     = "serviceAccount:${google_service_account.ti_analytics_readonly.email}"
}

resource "google_project_iam_member" "analytics_job_user" {
  project = var.project_id
  role    = "roles/bigquery.jobUser"
  member  = "serviceAccount:${google_service_account.ti_analytics_readonly.email}"
}

# 7) Visualization Storage read-only -> Object Viewer + List on all buckets
resource "google_storage_bucket_iam_member" "viz_ro_students" {
  bucket = google_storage_bucket.students_bucket.name
  role   = "roles/storage.objectViewer"
  member = "serviceAccount:${google_service_account.ti_viz_readonly.email}"
}
resource "google_storage_bucket_iam_member" "viz_ro_students_list" {
  bucket = google_storage_bucket.students_bucket.name
  role   = "roles/storage.legacyBucketReader"
  member = "serviceAccount:${google_service_account.ti_viz_readonly.email}"
}

resource "google_storage_bucket_iam_member" "viz_ro_etl" {
  bucket = google_storage_bucket.etl_bucket.name
  role   = "roles/storage.objectViewer"
  member = "serviceAccount:${google_service_account.ti_viz_readonly.email}"
}
resource "google_storage_bucket_iam_member" "viz_ro_etl_list" {
  bucket = google_storage_bucket.etl_bucket.name
  role   = "roles/storage.legacyBucketReader"
  member = "serviceAccount:${google_service_account.ti_viz_readonly.email}"
}

resource "google_storage_bucket_iam_member" "viz_ro_instructor" {
  bucket = google_storage_bucket.instructor_bucket.name
  role   = "roles/storage.objectViewer"
  member = "serviceAccount:${google_service_account.ti_viz_readonly.email}"
}
resource "google_storage_bucket_iam_member" "viz_ro_instructor_list" {
  bucket = google_storage_bucket.instructor_bucket.name
  role   = "roles/storage.legacyBucketReader"
  member = "serviceAccount:${google_service_account.ti_viz_readonly.email}"
}

# 8) Visualization Storage read-write -> Get/Put/List (no delete) on students bucket
resource "google_storage_bucket_iam_member" "viz_rw_students_creator" {
  bucket = google_storage_bucket.students_bucket.name
  role   = "roles/storage.objectCreator"
  member = "serviceAccount:${google_service_account.ti_viz_readwrite.email}"
}
resource "google_storage_bucket_iam_member" "viz_rw_students_viewer" {
  bucket = google_storage_bucket.students_bucket.name
  role   = "roles/storage.objectViewer"
  member = "serviceAccount:${google_service_account.ti_viz_readwrite.email}"
}
resource "google_storage_bucket_iam_member" "viz_rw_students_list" {
  bucket = google_storage_bucket.students_bucket.name
  role   = "roles/storage.legacyBucketReader"
  member = "serviceAccount:${google_service_account.ti_viz_readwrite.email}"
}

# 9) Lambda user analogue -> Cloud Functions Developer (project level)
resource "google_project_iam_member" "lambda_cloudfunctions_dev" {
  project = var.project_id
  role    = "roles/cloudfunctions.developer"
  member  = "serviceAccount:${google_service_account.lambda_user.email}"
}

# ----------------------------
# Outputs
# ----------------------------
output "buckets" {
  value = {
    students_bucket   = google_storage_bucket.students_bucket.name
    etl_bucket        = google_storage_bucket.etl_bucket.name
    instructor_bucket = google_storage_bucket.instructor_bucket.name
  }
}

output "bigquery_dataset" {
  value = google_bigquery_dataset.analytics_ds.dataset_id
}

output "service_accounts" {
  value = {
    ti_devopsadmin          = google_service_account.ti_devopsadmin.email
    ti_instructor_storage   = google_service_account.ti_instructor_storage.email
    ti_developer_storage    = google_service_account.ti_developer_storage.email
    ti_instructor_etl       = google_service_account.ti_instructor_etl.email
    ti_developer_etl        = google_service_account.ti_developer_etl.email
    ti_analytics_readonly   = google_service_account.ti_analytics_readonly.email
    ti_viz_readonly         = google_service_account.ti_viz_readonly.email
    ti_viz_readwrite        = google_service_account.ti_viz_readwrite.email
    lambda_user             = google_service_account.lambda_user.email
  }
}
