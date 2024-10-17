terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = "4.3.0"
    }
  }
}

provider "azurerm" {
  use_oidc = true
  features {
    resource_group {
       prevent_deletion_if_contains_resources = false
     }
  }
  subscription_id = "96526da7-b9bf-4757-a6ad-90a39cbdb171"
}
