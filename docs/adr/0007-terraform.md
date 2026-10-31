# ADR 0007: Terraform instead of CloudFormation

## Context
Auth (Cognito) and the agenda parser were CloudFormation stacks. The project already reaches outside one AWS stack, and a second environment is likely. Lab 5 (reports.yml) was not done, so two templates were migrated, not three.

## Decision
- Terraform with one root module in infra/ and one HCP Terraform workspace (successfulsuccess-dev), run remotely.
- Existing resources were adopted, not re-created: Retain on the stacks, stacks deleted, then import blocks. Result: 10 imported, 2 created (aws_lambda_permission, no data), 0 destroyed.
- ignore_changes on the user pool schema, the app client generate_secret and the Google provider_details, because they cannot be read back after import.
- Apply happens only in HCP Terraform with short-lived OIDC credentials. No AWS keys are stored.

## Alternatives considered
- CloudFormation: no state to keep, but AWS-only.
- CDK: still CloudFormation underneath.
- OpenTofu: same files, but HCP Terraform integration is simpler with Terraform.

## Consequences
- Who changes infrastructure: anyone who can push to main, after reading the plan in HCP Terraform.
- Secrets: the Google client secret lives in Cognito and in the Terraform state (HCP Terraform, access-controlled), not in Git.
- If HCP Terraform is down, the deployed system keeps running; infrastructure changes wait.
- The bootstrap role has AdministratorAccess and trusts any workspace of the organization; it should be narrowed.
