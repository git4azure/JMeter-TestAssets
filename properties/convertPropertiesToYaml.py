import sys
import collections
from configobj import ConfigObj


def convert_properties_to_yaml():
    # Read the file name from command line argument
    input_file = sys.argv[1]
    # Read key=value property configs in python dictionary
    config_dict = ConfigObj(input_file)
    # Store the result in yaml_dict
    yaml_dict = {}

    yaml_file = open(input_file + '.yaml', 'w')
    yaml_file.write("execution:\n")
    yaml_file.write("- scenario: relative-perf\n")
    yaml_file.write("  relative-perf:\n")
    yaml_file.write("    script: ToBeOverWrittenOnCommandLine.jmx\n")
# Fail the test if these basic criteria fail - we dont want to use a duff test
    yaml_file.write("reporting:\n")
    yaml_file.write("  - module: passfail\n")
    yaml_file.write("    criteria:\n")
    # Average response time over x then stop the test immediately as failed
    # Docs for this can be found in: https://gettaurus.org/docs/PassFail/
    yaml_file.write("    - avg-rt>30s for 120s, stop as failed\n")
    # Average connect time
    yaml_file.write("    - avg-ct>100ms for 120s, stop as failed\n")
    # Number of failed transactions
    yaml_file.write("    - failures>50% for 30s, stop as failed\n")
    # Error 5xx's more than 20% of requests for 2 minutes
    yaml_file.write("    - rc5??>20% for 120s, stop as failed\n")
    # Check to make sure CPU is not maxed out on Jenkins server itself as this will affect results
    # This is only a warning however, the test will not fail
    yaml_file.write("    - class: bzt.modules.monitoring.MonitoringCriteria\n")
    yaml_file.write("      subject: local/cpu\n")
    yaml_file.write("      condition: '>'\n")
    yaml_file.write("      threshold: 90\n")
    yaml_file.write("      timeframe: 30s\n")
    yaml_file.write("      fail: false\n")
    yaml_file.write("      stop: false\n")

    yaml_file.write("modules:\n")
    yaml_file.write("  consolidator:\n")
    yaml_file.write("    ignore-labels:\n")
    yaml_file.write("    - BS-MultiStoreUserJourneyHelper\n")
    yaml_file.write("    - BS-MultiStoreThreadSetup\n")
    yaml_file.write("    - BS-MultiStoreSiteHelper\n")
    yaml_file.write("  jmeter:\n")
    yaml_file.write("    plugins:\n")
    yaml_file.write("    - jpgc-ggl\n")
    yaml_file.write("    - jpgc-synthesis\n")
    yaml_file.write("    - jpgc-graphs-basic\n")
    yaml_file.write("    - jpgc-graphs-vs\n")
    yaml_file.write("    - jpgc-graphs-additional\n")
    yaml_file.write("    - jpgc-graphs-dist\n")
    yaml_file.write("    - jpgc-graphs-composite\n")
    yaml_file.write("    properties:")
# Settings to provide Graph output 
    yaml_file.write("\n      jmeter.save.saveservice.output_format: csv")
    yaml_file.write("\n      jmeter.save.saveservice.data_type: false")
    yaml_file.write("\n      jmeter.save.saveservice.label: true")
    yaml_file.write("\n      jmeter.save.saveservice.response_code: true")
    yaml_file.write("\n      jmeter.save.saveservice.response_data.on_error: false")
    yaml_file.write("\n      jmeter.save.saveservice.response_message: false")
    yaml_file.write("\n      jmeter.save.saveservice.assertion_results_failure_message: false")
    yaml_file.write("\n      jmeter.save.saveservice.successful: true")
    yaml_file.write("\n      jmeter.save.saveservice.thread_name: true")
    yaml_file.write("\n      jmeter.save.saveservice.time: true")
    yaml_file.write("\n      jmeter.save.saveservice.subresults: false")
    yaml_file.write("\n      jmeter.save.saveservice.assertions: true")
    yaml_file.write("\n      jmeter.save.saveservice.latency: true")
    yaml_file.write("\n      jmeter.save.saveservice.bytes: true")
    yaml_file.write("\n      jmeter.save.saveservice.hostname: true")
    yaml_file.write("\n      jmeter.save.saveservice.thread_counts: true")
    yaml_file.write("\n      jmeter.save.saveservice.sample_count: true")
    yaml_file.write("\n      jmeter.save.saveservice.timestamp_format: \"HH:mm:ss\"")
    yaml_file.write("\n      jmeter.save.saveservice.default_delimiter: \";\"")
    yaml_file.write("\n      jmeter.save.saveservice.print_field_names: true")
    yaml_file.write("\n      jmeter.save.saveservice.autoflush: true")
    for key, value in config_dict.items():
        yaml_file.write("\n      " + key + ": " + value)
convert_properties_to_yaml()