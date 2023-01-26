# Payment Gateway
This is a simple Payment Gateway application written in Python using aiohttp.

# Running the Payment Gateway
## Using Terraform
1. Make sure you have [Terraform](https://www.terraform.io/) and [AWS CLI](https://aws.amazon.com/cli/) installed on your machine.
2. Clone this repository and navigate to the root directory of the project.
3. Run `terraform init` to initialize your provider and backend.
4. Update the `main.tf` file with your AWS credentials and any other necessary configuration.
5. Run `terraform apply` to create the resources.
6. To destroy the resources, run `terraform destroy`.

## Without Terraform
For installing project dependencies using poetry:
`poetry install`
For running project:
`poetry run python main.py`

## Testing
Run `poetry run pytest` to execute the test suite.

## Scaling
You can adjust the number of servers running the Payment Gateway application by modifying the `count` argument in the `main.tf` file.
You can also adjust the resources allocated to each server by modifying the `instance_type` argument in the `main.tf` file.
