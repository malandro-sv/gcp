#! /usr/bin/env python3
import sys
from time import sleep
from datetime import timedelta
from google.cloud import monitoring_v3
from google.api_core import exceptions

client = monitoring_v3.MetricServiceClient()
project_name = f"projects/PROJECT_ID"
metric =  {"name": "projects/PROJECT_ID",
           "type": f"custom.googleapis.com/{sys.argv[1]}",
           "labels": [
               { "key": sys.argv[2],
                "value_type": "STRING",
                "description": f"{sys.argv[2]} names"}],
           "metric_kind": "GAUGE",
           "value_type": "INT64",
           "unit": "1",
           "description": "Tinkering to fetch metadata.",
           "display_name": sys.argv[1],
           "launch_stage": "GA",
           "monitored_resource_types": [
               "gce_instance",
               "k8s_container",
               "baremetalsolution.googleapis.com/Instance",
               "aiplatform.googleapis.com/Endpoint"
               ], # ----- field of interest: metadata ----- #
           "metadata": {
               "sample_period": timedelta(seconds=1),
               "ingest_delay": timedelta(seconds=2),
               "time_series_resource_hierarchy_level": [ "PROJECT"]
               }, # ----- metada ends ----- #
           }

try:
    full_descriptor_path= f"{project_name}/metricDescriptors/{metric['type']}"
    print(f"Checking if {metric['type']} exists in {project_name}...")
    client.get_metric_descriptor(name=full_descriptor_path)
except exceptions.NotFound:
    print(f"{metric['type']} not found. Attempting to create...")
    client.create_metric_descriptor(
            name=project_name, metric_descriptor=metric)
    print(f"{metric['type']} successfully created.")
    sleep(7)
    print(full_descriptor_path)
    client.get_metric_descriptor(name=full_descriptor_path)
except exceptions.GoogleAPICallError as error:
    print(f"GCP API error {error.code}:  {error.message}")
except Exception as error:
    print(f"System Error - {error}")
else:
    print(f"{metric['type']} already exists. Nothing to do.")
