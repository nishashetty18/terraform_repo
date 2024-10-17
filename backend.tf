terraform {
   backend "azurerm" {
    resource_group_name  = "test-rg"
    storage_account_name  = "demostorage64748"
    container_name        = "demostorage64748container"
    key                   = "terraform.tfstate"
   }
}

