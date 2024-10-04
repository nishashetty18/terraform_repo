terraform {
  
  backend "azurerm" {
     resource_group_name  = "test-rg"
    storage_account_name  = "samplestorageaccount768"
    container_name        = "samplestorageaccount768container"
    key                   = "terraform.tfstate"
    
  }
}