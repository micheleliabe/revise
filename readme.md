# Revise.cli

## Overview
Revise.cli is a command-line interface (CLI) tool designed to help manage and optimize cloud resources across multiple cloud providers. It currently provides functionalities for analyzing AWS resources, offering recommendations for cost optimization and security improvements.

## Features
- Analyze AWS resources for cost optimization and security improvements.
  - Identifying unused Elastic IPs.
  - Locating security groups with inbound rules allowing traffic from 0.0.0.0/0.
  - Detecting RDS instances with public IPs (publicly accessible).
  - Finding in-use GP2 volumes.
  - Identifying detached volumes.
  - Identifying volumes attached on stopped EC2 instances

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/micheleliabe/revise.git
   ```

2. Navigate to the project directory:
   ```
   cd revise
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
- Displays cost optimization recommendations for AWS resources in the specified region.

```
./revise.py aws costs --region all
```
- Displays cost optimization recommendations for AWS resources in all regions.

#### Security
```
./revise.py aws security --region us-east-1
```
- Provides security recommendations for AWS resources in the specified region.

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