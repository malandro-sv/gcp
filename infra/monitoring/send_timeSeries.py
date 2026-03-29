#! /usr/bin/env python3
import sys, time, random
from datetime import datetime
from google.cloud import monitoring_v3
project_name = f"projects/manuelafg-dev922"

def create_metric_series():
    """ metric descriptor full name:
    projects/PROJECT_ID/metricDescriptors/custom.googleapis.com/FOO
    all values but metric.labels hard coded for troubleshooting only """
    client = monitoring_v3.MetricServiceClient()
    try:
        while True:
            series = monitoring_v3.TimeSeries()
            series.metric.type = f"custom.googleapis.com/{sys.argv[1]}"
            series.resource.type = "gce_instance"
            series.resource.labels["instance_id"] = INSTANCE_ID
            series.resource.labels["zone"] = ZONE
            distro = series.metric.labels[sys.argv[2]] = sys.argv[3]
            #kernel = series.metric.labels["kernel"] = sys.argv[2]

            # Get current timestamp
            now = time.time()
            seconds = int(now)
            nanos = int((now - seconds) **2)
            val = random.uniform(0, 65)
            interval = monitoring_v3.TimeInterval({"end_time":
                                                   {"seconds": seconds}})
                                                   #{"seconds": seconds,
                                                    #"nanos": nanos}})
            point = monitoring_v3.Point({"interval": interval,
                                         "value": {"int64_value": val}})
            series.points = [point]

            # Send metric
            client.create_time_series(name=project_name, time_series=[series])
            # console log - not an actual log. might need to use metadata section to achieve proper logging? #TODO
            print(f"< Datapoint {val} sent to '{sys.argv[1]}'",
            f"on {datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')} />")
            time.sleep(4)
    except KeyboardInterrupt:
        print("\nScript terminated by user")
        sys.exit(0)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
       sys.exit(1)

if __name__ == "__main__":
    print("Starting metric collection. Press Ctrl+C to stop.")
    create_metric_series()
