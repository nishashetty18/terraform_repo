resource "azurerm_resource_group" "example" {
  name     = var.name
  location = var.location
}
resource "azurerm_storage_account" "storageaccount" {
  name                     = var.strorageacountname
  resource_group_name      = azurerm_resource_group.example.name
  location                 = azurerm_resource_group.example.location
  account_tier             = "Standard"
  account_replication_type = "LRS"

  tags = {
    environment = "staging"
  }
}
resource "azurerm_storage_container" "res-storage-container" {
  name                  = "${var.strorageacountname}container"
  storage_account_name  = azurerm_storage_account.storageaccount.name
  container_access_type = "private"
}




