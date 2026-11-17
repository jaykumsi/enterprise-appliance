# How to run (Snowflake RBAC version inspired by your AWS IAM policies)
# 1. Go to the folder you want to execute the run
# 2. terraform init
# 3. terraform plan
# 4. terraform apply
#
# Notes:
# - Snowflake doesn't use AWS-style IAM policies; it uses roles + grants (RBAC).
# - This file creates:
#     - 1 database + several schemas (to mimic "domains" like instructor/etl/analytics/students)
#     - a few warehouses (compute)
#     - roles for devopsadmin/instructor/developer/analytics/viz/etc
#     - grants using the *new* grant resources (grant_privileges_to_account_role, grant_account_role)
#
# Where "Athena" fits:
# - In AWS, Athena is a serverless SQL query service.
# - In Snowflake, querying is native (warehouse + database objects). So "Athena read-only" maps to an
#   analytics read-only role on an analytics schema + warehouse USAGE.
#
# Provider note:
# - Snowflake provider had a major grants redesign; old *_grant resources were deprecated/removed.
#   Use `snowflake_grant_privileges_to_account_role` etc as shown in Snowflake's official Terraform guide. citeturn9view2turn9view3

terraform {
  required_version = ">= 1.5.0"

  required_providers {
    snowflake = {
      source  = "snowflakedb/snowflake"
      version = ">= 2.0.0"
    }
  }
}

# ----------------------------
# Variables
# ----------------------------
variable "organization_name" {
  type        = string
  description = "Snowflake organization name (lowercase). Example: abcdefg"
}

variable "account_name" {
  type        = string
  description = "Snowflake account name (lowercase). Example: xy12345"
}

variable "terraform_user" {
  type        = string
  default     = "TERRAFORM_SVC"
  description = "Snowflake service user that Terraform authenticates as"
}

variable "private_key_path" {
  type        = string
  default     = "~/.ssh/snowflake_tf_snow_key.p8"
  description = "Path to the RSA private key (PKCS8) for SNOWFLAKE_JWT authentication"
}

# ----------------------------
# Providers
# ----------------------------
# SYSADMIN: create DB/warehouse objects
provider "snowflake" {
  organization_name = var.organization_name
  account_name      = var.account_name
  user              = var.terraform_user
  role              = "SYSADMIN"
  authenticator     = "SNOWFLAKE_JWT"
  private_key       = file(var.private_key_path)
}

# USERADMIN: create users/roles and manage grants to users/roles
provider "snowflake" {
  organization_name = var.organization_name
  account_name      = var.account_name
  user              = var.terraform_user
  role              = "USERADMIN"
  authenticator     = "SNOWFLAKE_JWT"
  private_key       = file(var.private_key_path)
  alias             = "useradmin"
}

# ----------------------------
# Core objects: DB, Schemas, Warehouses
# ----------------------------
resource "snowflake_database" "ti_db" {
  name         = "TI_TRAINING_DB"
  is_transient = false
}

resource "snowflake_schema" "instructor_sc" {
  name                = "INSTRUCTOR"
  database            = snowflake_database.ti_db.name
  with_managed_access = false
}

resource "snowflake_schema" "etl_sc" {
  name                = "ETL"
  database            = snowflake_database.ti_db.name
  with_managed_access = false
}

resource "snowflake_schema" "analytics_sc" {
  name                = "ANALYTICS"
  database            = snowflake_database.ti_db.name
  with_managed_access = false
}

resource "snowflake_schema" "students_sc" {
  name                = "STUDENTS"
  database            = snowflake_database.ti_db.name
  with_managed_access = false
}

resource "snowflake_schema" "functions_sc" {
  name                = "FUNCTIONS"
  database            = snowflake_database.ti_db.name
  with_managed_access = false
}

resource "snowflake_warehouse" "ti_wh" {
  name                      = "TI_WH"
  warehouse_type            = "STANDARD"
  warehouse_size            = "XSMALL"
  auto_suspend              = 60
  auto_resume               = true
  enable_query_acceleration = false
  initially_suspended       = true
  max_cluster_count         = 1
  min_cluster_count         = 1
}

resource "snowflake_warehouse" "ti_etl_wh" {
  name                      = "TI_ETL_WH"
  warehouse_type            = "STANDARD"
  warehouse_size            = "XSMALL"
  auto_suspend              = 60
  auto_resume               = true
  enable_query_acceleration = false
  initially_suspended       = true
  max_cluster_count         = 1
  min_cluster_count         = 1
}

resource "snowflake_warehouse" "ti_viz_wh" {
  name                      = "TI_VIZ_WH"
  warehouse_type            = "STANDARD"
  warehouse_size            = "XSMALL"
  auto_suspend              = 60
  auto_resume               = true
  enable_query_acceleration = false
  initially_suspended       = true
  max_cluster_count         = 1
  min_cluster_count         = 1
}

# ----------------------------
# Roles (account roles)
# ----------------------------
resource "snowflake_account_role" "ti_devopsadmin" {
  provider = snowflake.useradmin
  name     = "TI_DEVOPSADMIN"
  comment  = "Broad admin role for TI training resources"
}

resource "snowflake_account_role" "ti_instructor" {
  provider = snowflake.useradmin
  name     = "TI_INSTRUCTOR"
  comment  = "Instructor role (read/write in INSTRUCTOR schema)"
}

resource "snowflake_account_role" "ti_etl_developer" {
  provider = snowflake.useradmin
  name     = "TI_ETL_DEVELOPER"
  comment  = "ETL developer role (read/write limited in ETL schema)"
}

resource "snowflake_account_role" "ti_etl_instructor" {
  provider = snowflake.useradmin
  name     = "TI_ETL_INSTRUCTOR"
  comment  = "ETL instructor role (more privileges in ETL schema)"
}

resource "snowflake_account_role" "ti_analytics_readonly" {
  provider = snowflake.useradmin
  name     = "TI_ANALYTICS_READONLY"
  comment  = "Analytics read-only role (SELECT in ANALYTICS schema)"
}

resource "snowflake_account_role" "ti_viz_readonly" {
  provider = snowflake.useradmin
  name     = "TI_VIZ_READONLY"
  comment  = "Visualization read-only role (SELECT in STUDENTS schema)"
}

resource "snowflake_account_role" "ti_viz_readwrite" {
  provider = snowflake.useradmin
  name     = "TI_VIZ_READWRITE"
  comment  = "Visualization read-write role (SELECT/INSERT in STUDENTS schema)"
}

resource "snowflake_account_role" "lambda_role" {
  provider = snowflake.useradmin
  name     = "TI_LAMBDA_USER"
  comment  = "Lambda analogue role (create functions/procedures in FUNCTIONS schema)"
}

# Best practice: grant custom roles to SYSADMIN so your account has a clear hierarchy (optional).
# (This does NOT give the custom roles SYSADMIN powers; it just places them under SYSADMIN.) citeturn9view2
resource "snowflake_grant_account_role" "grant_roles_to_sysadmin" {
  provider         = snowflake.useradmin
  for_each         = toset([
    snowflake_account_role.ti_devopsadmin.name,
    snowflake_account_role.ti_instructor.name,
    snowflake_account_role.ti_etl_developer.name,
    snowflake_account_role.ti_etl_instructor.name,
    snowflake_account_role.ti_analytics_readonly.name,
    snowflake_account_role.ti_viz_readonly.name,
    snowflake_account_role.ti_viz_readwrite.name,
    snowflake_account_role.lambda_role.name
  ])
  role_name        = each.value
  parent_role_name = "SYSADMIN"
}

# ----------------------------
# Grants (new grant resources)
# ----------------------------
# Helper locals for fully qualified schema names (FQN is recommended). citeturn9view2
locals {
  instructor_schema_fqn = snowflake_schema.instructor_sc.fully_qualified_name
  etl_schema_fqn        = snowflake_schema.etl_sc.fully_qualified_name
  analytics_schema_fqn  = snowflake_schema.analytics_sc.fully_qualified_name
  students_schema_fqn   = snowflake_schema.students_sc.fully_qualified_name
  functions_schema_fqn  = snowflake_schema.functions_sc.fully_qualified_name
}

# --- DevOps Admin (broad within this training DB) ---
# USAGE on DB
resource "snowflake_grant_privileges_to_account_role" "devops_usage_db" {
  provider          = snowflake.useradmin
  account_role_name = snowflake_account_role.ti_devopsadmin.name
  privileges        = ["USAGE"]

  on_account_object {
    object_type = "DATABASE"
    object_name = snowflake_database.ti_db.name
  }
}

# USAGE on all schemas
resource "snowflake_grant_privileges_to_account_role" "devops_usage_schemas" {
  provider          = snowflake.useradmin
  account_role_name = snowflake_account_role.ti_devopsadmin.name
  privileges        = ["USAGE"]

  for_each = toset([
    local.instructor_schema_fqn,
    local.etl_schema_fqn,
    local.analytics_schema_fqn,
    local.students_schema_fqn,
    local.functions_schema_fqn
  ])

  on_schema {
    schema_name = each.value
  }
}

# Warehouse USAGE/OPERATE on all training warehouses
resource "snowflake_grant_privileges_to_account_role" "devops_wh" {
  provider          = snowflake.useradmin
  account_role_name = snowflake_account_role.ti_devopsadmin.name
  privileges        = ["USAGE", "OPERATE"]

  for_each = toset([
    snowflake_warehouse.ti_wh.name,
    snowflake_warehouse.ti_etl_wh.name,
    snowflake_warehouse.ti_viz_wh.name
  ])

  on_account_object {
    object_type = "WAREHOUSE"
    object_name = each.value
  }
}

# --- Instructor (read/write in INSTRUCTOR schema) ---
resource "snowflake_grant_privileges_to_account_role" "instructor_usage_db" {
  provider          = snowflake.useradmin
  account_role_name = snowflake_account_role.ti_instructor.name
  privileges        = ["USAGE"]

  on_account_object {
    object_type = "DATABASE"
    object_name = snowflake_database.ti_db.name
  }
}

resource "snowflake_grant_privileges_to_account_role" "instructor_usage_schema" {
  provider          = snowflake.useradmin
  account_role_name = snowflake_account_role.ti_instructor.name
  privileges        = ["USAGE", "CREATE TABLE", "CREATE VIEW"]

  on_schema {
    schema_name = local.instructor_schema_fqn
  }
}

# DML on all current tables in INSTRUCTOR schema
resource "snowflake_grant_privileges_to_account_role" "instructor_tables_all" {
  provider          = snowflake.useradmin
  account_role_name = snowflake_account_role.ti_instructor.name
  privileges        = ["SELECT", "INSERT", "UPDATE", "DELETE"]

  on_schema_object {
    all {
      object_type_plural = "TABLES"
      in_schema          = local.instructor_schema_fqn
    }
  }
}

# DML on future tables in INSTRUCTOR schema
resource "snowflake_grant_privileges_to_account_role" "instructor_tables_future" {
  provider          = snowflake.useradmin
  account_role_name = snowflake_account_role.ti_instructor.name
  privileges        = ["SELECT", "INSERT", "UPDATE", "DELETE"]

  on_schema_object {
    future {
      object_type_plural = "TABLES"
      in_schema          = local.instructor_schema_fqn
    }
  }
}

# --- ETL Instructor (more privileges in ETL schema) ---
resource "snowflake_grant_privileges_to_account_role" "etl_instructor_usage_schema" {
  provider          = snowflake.useradmin
  account_role_name = snowflake_account_role.ti_etl_instructor.name
  privileges        = ["USAGE", "CREATE TABLE", "CREATE VIEW", "CREATE STAGE", "CREATE PIPE", "CREATE TASK", "CREATE STREAM"]

  on_schema {
    schema_name = local.etl_schema_fqn
  }
}

resource "snowflake_grant_privileges_to_account_role" "etl_instructor_tables_all" {
  provider          = snowflake.useradmin
  account_role_name = snowflake_account_role.ti_etl_instructor.name
  privileges        = ["SELECT", "INSERT", "UPDATE", "DELETE"]

  on_schema_object {
    all {
      object_type_plural = "TABLES"
      in_schema          = local.etl_schema_fqn
    }
  }
}

resource "snowflake_grant_privileges_to_account_role" "etl_instructor_tables_future" {
  provider          = snowflake.useradmin
  account_role_name = snowflake_account_role.ti_etl_instructor.name
  privileges        = ["SELECT", "INSERT", "UPDATE", "DELETE"]

  on_schema_object {
    future {
      object_type_plural = "TABLES"
      in_schema          = local.etl_schema_fqn
    }
  }
}

# ETL warehouse usage
resource "snowflake_grant_privileges_to_account_role" "etl_instructor_wh" {
  provider          = snowflake.useradmin
  account_role_name = snowflake_account_role.ti_etl_instructor.name
  privileges        = ["USAGE"]

  on_account_object {
    object_type = "WAREHOUSE"
    object_name = snowflake_warehouse.ti_etl_wh.name
  }
}

# --- ETL Developer (limited: read + insert; no delete) ---
resource "snowflake_grant_privileges_to_account_role" "etl_dev_usage_schema" {
  provider          = snowflake.useradmin
  account_role_name = snowflake_account_role.ti_etl_developer.name
  privileges        = ["USAGE"]

  on_schema {
    schema_name = local.etl_schema_fqn
  }
}

resource "snowflake_grant_privileges_to_account_role" "etl_dev_tables_all" {
  provider          = snowflake.useradmin
  account_role_name = snowflake_account_role.ti_etl_developer.name
  privileges        = ["SELECT", "INSERT"]

  on_schema_object {
    all {
      object_type_plural = "TABLES"
      in_schema          = local.etl_schema_fqn
    }
  }
}

resource "snowflake_grant_privileges_to_account_role" "etl_dev_tables_future" {
  provider          = snowflake.useradmin
  account_role_name = snowflake_account_role.ti_etl_developer.name
  privileges        = ["SELECT", "INSERT"]

  on_schema_object {
    future {
      object_type_plural = "TABLES"
      in_schema          = local.etl_schema_fqn
    }
  }
}

resource "snowflake_grant_privileges_to_account_role" "etl_dev_wh" {
  provider          = snowflake.useradmin
  account_role_name = snowflake_account_role.ti_etl_developer.name
  privileges        = ["USAGE"]

  on_account_object {
    object_type = "WAREHOUSE"
    object_name = snowflake_warehouse.ti_etl_wh.name
  }
}

# --- Analytics read-only (Athena read-only analogue) ---
resource "snowflake_grant_privileges_to_account_role" "analytics_usage_schema" {
  provider          = snowflake.useradmin
  account_role_name = snowflake_account_role.ti_analytics_readonly.name
  privileges        = ["USAGE"]

  on_schema {
    schema_name = local.analytics_schema_fqn
  }
}

resource "snowflake_grant_privileges_to_account_role" "analytics_select_all_tables" {
  provider          = snowflake.useradmin
  account_role_name = snowflake_account_role.ti_analytics_readonly.name
  privileges        = ["SELECT"]

  on_schema_object {
    all {
      object_type_plural = "TABLES"
      in_schema          = local.analytics_schema_fqn
    }
  }
}

resource "snowflake_grant_privileges_to_account_role" "analytics_select_future_tables" {
  provider          = snowflake.useradmin
  account_role_name = snowflake_account_role.ti_analytics_readonly.name
  privileges        = ["SELECT"]

  on_schema_object {
    future {
      object_type_plural = "TABLES"
      in_schema          = local.analytics_schema_fqn
    }
  }
}

resource "snowflake_grant_privileges_to_account_role" "analytics_wh" {
  provider          = snowflake.useradmin
  account_role_name = snowflake_account_role.ti_analytics_readonly.name
  privileges        = ["USAGE"]

  on_account_object {
    object_type = "WAREHOUSE"
    object_name = snowflake_warehouse.ti_wh.name
  }
}

# --- Visualization read-only / read-write (students schema) ---
resource "snowflake_grant_privileges_to_account_role" "viz_ro_usage_schema" {
  provider          = snowflake.useradmin
  account_role_name = snowflake_account_role.ti_viz_readonly.name
  privileges        = ["USAGE"]

  on_schema {
    schema_name = local.students_schema_fqn
  }
}

resource "snowflake_grant_privileges_to_account_role" "viz_ro_select_all_tables" {
  provider          = snowflake.useradmin
  account_role_name = snowflake_account_role.ti_viz_readonly.name
  privileges        = ["SELECT"]

  on_schema_object {
    all {
      object_type_plural = "TABLES"
      in_schema          = local.students_schema_fqn
    }
  }
}

resource "snowflake_grant_privileges_to_account_role" "viz_ro_select_future_tables" {
  provider          = snowflake.useradmin
  account_role_name = snowflake_account_role.ti_viz_readonly.name
  privileges        = ["SELECT"]

  on_schema_object {
    future {
      object_type_plural = "TABLES"
      in_schema          = local.students_schema_fqn
    }
  }
}

resource "snowflake_grant_privileges_to_account_role" "viz_rw_usage_schema" {
  provider          = snowflake.useradmin
  account_role_name = snowflake_account_role.ti_viz_readwrite.name
  privileges        = ["USAGE"]

  on_schema {
    schema_name = local.students_schema_fqn
  }
}

# Read + write (no delete) on all/future tables
resource "snowflake_grant_privileges_to_account_role" "viz_rw_tables_all" {
  provider          = snowflake.useradmin
  account_role_name = snowflake_account_role.ti_viz_readwrite.name
  privileges        = ["SELECT", "INSERT", "UPDATE"]

  on_schema_object {
    all {
      object_type_plural = "TABLES"
      in_schema          = local.students_schema_fqn
    }
  }
}

resource "snowflake_grant_privileges_to_account_role" "viz_rw_tables_future" {
  provider          = snowflake.useradmin
  account_role_name = snowflake_account_role.ti_viz_readwrite.name
  privileges        = ["SELECT", "INSERT", "UPDATE"]

  on_schema_object {
    future {
      object_type_plural = "TABLES"
      in_schema          = local.students_schema_fqn
    }
  }
}

resource "snowflake_grant_privileges_to_account_role" "viz_wh" {
  provider          = snowflake.useradmin
  account_role_name = snowflake_account_role.ti_viz_readonly.name
  privileges        = ["USAGE"]

  on_account_object {
    object_type = "WAREHOUSE"
    object_name = snowflake_warehouse.ti_viz_wh.name
  }
}

resource "snowflake_grant_privileges_to_account_role" "viz_wh_rw" {
  provider          = snowflake.useradmin
  account_role_name = snowflake_account_role.ti_viz_readwrite.name
  privileges        = ["USAGE"]

  on_account_object {
    object_type = "WAREHOUSE"
    object_name = snowflake_warehouse.ti_viz_wh.name
  }
}

# --- Lambda analogue (create functions/procedures in FUNCTIONS schema) ---
resource "snowflake_grant_privileges_to_account_role" "lambda_usage_schema" {
  provider          = snowflake.useradmin
  account_role_name = snowflake_account_role.lambda_role.name
  privileges        = ["USAGE", "CREATE FUNCTION", "CREATE PROCEDURE"]

  on_schema {
    schema_name = local.functions_schema_fqn
  }
}

resource "snowflake_grant_privileges_to_account_role" "lambda_wh" {
  provider          = snowflake.useradmin
  account_role_name = snowflake_account_role.lambda_role.name
  privileges        = ["USAGE"]

  on_account_object {
    object_type = "WAREHOUSE"
    object_name = snowflake_warehouse.ti_wh.name
  }
}

# ----------------------------
# Outputs
# ----------------------------
output "database" {
  value = snowflake_database.ti_db.name
}

output "schemas" {
  value = {
    instructor = local.instructor_schema_fqn
    etl        = local.etl_schema_fqn
    analytics  = local.analytics_schema_fqn
    students   = local.students_schema_fqn
    functions  = local.functions_schema_fqn
  }
}

output "warehouses" {
  value = {
    default_wh = snowflake_warehouse.ti_wh.name
    etl_wh     = snowflake_warehouse.ti_etl_wh.name
    viz_wh     = snowflake_warehouse.ti_viz_wh.name
  }
}

output "roles" {
  value = {
    ti_devopsadmin        = snowflake_account_role.ti_devopsadmin.name
    ti_instructor         = snowflake_account_role.ti_instructor.name
    ti_etl_developer      = snowflake_account_role.ti_etl_developer.name
    ti_etl_instructor     = snowflake_account_role.ti_etl_instructor.name
    ti_analytics_readonly = snowflake_account_role.ti_analytics_readonly.name
    ti_viz_readonly       = snowflake_account_role.ti_viz_readonly.name
    ti_viz_readwrite      = snowflake_account_role.ti_viz_readwrite.name
    ti_lambda_user        = snowflake_account_role.lambda_role.name
  }
}
