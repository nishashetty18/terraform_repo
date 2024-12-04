terraform {
   backend "azurerm" {
    resource_group_name   = "yghujk"
    storage_account_name  = "mystorage78967"
    container_name        = "mycontainer89"
    key                   = "terraform.tfstate"
   }
}

