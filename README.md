# Prometheus and Grafana Application

This project sets up a monitoring solution using Prometheus and Grafana within Docker containers. It allows you to collect metrics from various targets and visualize them through a customizable dashboard.

## Project Structure

```
prometheus-grafana-app
├── prometheus
│   ├── prometheus.yml
├── grafana
│   ├── provisioning
│   │   ├── dashboards
│   │   │   └── sample-dashboard.json
│   │   ├── datasources
│   │   │   └── datasource.yml
├── docker-compose.yml
└── README.md
```

## Setup Instructions

1. **Clone the Repository**
   Clone this repository to your local machine using:
   ```
   git clone <repository-url>
   cd prometheus-grafana-app
   ```

2. **Modify Configuration Files**
   - Update `prometheus/prometheus.yml` to define your scrape targets.
   - Adjust `grafana/provisioning/datasources/datasource.yml` to set the correct URL for your Prometheus instance.

3. **Start the Application**
   Use Docker Compose to start the services:
   ```
   docker-compose up -d
   ```

4. **Access Grafana**
   Open your web browser and navigate to `http://localhost:3000`. The default login is:
   - Username: admin
   - Password: admin (you will be prompted to change this on first login)

5. **View Metrics**
   Once logged in, you can access the sample dashboard provided in `grafana/provisioning/dashboards/sample-dashboard.json` to view the metrics collected by Prometheus.

## Usage Guidelines

- Ensure that your Prometheus targets are correctly configured in `prometheus/prometheus.yml`.
- You can create additional dashboards in Grafana by modifying or adding new JSON files in the `grafana/provisioning/dashboards` directory.
- For further customization, refer to the official documentation for Prometheus and Grafana.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for this project.