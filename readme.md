# Revise.cli

## Overview
Revise.cli is a command-line interface (CLI) tool designed to help manage and optimize cloud resources across multiple cloud providers. It currently provides functionalities for analyzing AWS resources, offering recommendations for cost optimization and security improvements.

## Features
- Analyze AWS resources for cost optimization and security improvements.
- Support for AWS cloud provider.
  - Identifying unused Elastic IPs.
  - Locating security groups with inbound rules allowing traffic from 0.0.0.0/0.
  - Detecting RDS instances with public IPs (publicly accessible).
  - Finding in-use GP2 volumes.
  - Identifying detached volumes.

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/your_username/revise-cli.git
   ```

2. Navigate to the project directory:
   ```
   cd revise-cli
   ```

3. Install dependencies using pip:
   ```
   pip install -r requirements.txt
   ```

## Usage
### AWS Commands
#### Costs
```
./revise.py aws costs --region us-east-1
```
- Displays cost optimization recommendations for AWS resources in the specified region, such as detached EBS volumes, GP2 volumes, and unused Elastic IPs.

```
./revise.py aws costs --region all
```
- Displays cost optimization recommendations for AWS resources in all regions.

#### Security
```
./revise.py aws security --region us-east-1
```
- Provides security recommendations for AWS resources in the specified region, including security groups with internet access and publicly accessible RDS instances.

```
./revise.py aws security --region all
```
- Provides security recommendations for AWS resources in all regions.

### Azure Commands (Under Development)
```
./revise.py azure ...
```
- Azure functionalities are currently under development and will be available soon.

### GCP Commands (Under Development)
```
./revise.py gcp ...
```
- GCP functionalities are currently under development and will be available soon.

## Contributing
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).

---

Esse README.md reflete a situação atual do projeto, com as funcionalidades do Azure e GCP ainda em desenvolvimento. As instruções foram atualizadas para incluir a necessidade de fornecer a região ao executar os comandos para análise de recursos da AWS.