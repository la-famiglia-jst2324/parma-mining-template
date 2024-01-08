variable "ANALYTICS_BASE_URL" {
  description = "value"
  type        = string
}

/* ------------------------ Analytics and Sourcing Auth Flow ------------------------ */

variable "SHARED_SECRET_KEY" {
  description = "Shared secret key for the analytics and sourcing auth flow"
  type        = string
  sensitive   = true
}
