#
# services.py - implementation of abstract class defining API for service specs.
#
# Copyright (c) 2017 SingularityNET
#
# Distributed under the MIT software license, see LICENSE file.
#

# Duration constants - durations are in milliseconds
from abc import ABC
from datetime import timedelta

ONE_SECOND = timedelta(seconds=1)
ONE_MINUTE = ONE_SECOND * 60
ONE_HOUR = ONE_MINUTE * 60


class ServiceDescriptor(ABC):
    def __init__(self, type_name, inputs, output, duration):
        self.type_name = type_name
        self.inputs = inputs
        self.output = output
        self.duration = duration

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __str__(self):
        return "<Service: %s, %s, %s, %s>" % (self.type_name, self.inputs, self.output, self.duration)

    @classmethod
    def test_services(cls) -> []:
        services = []
        services.append(ServiceDescriptor('ImageRecognition1', ['file-url'], 'file-url-put', ONE_HOUR))
        services.append(ServiceDescriptor('ImageRecognition2', ['file-url'], 'file-url-put', ONE_MINUTE))
        services.append(ServiceDescriptor('DocumentSummary1', ['file-url'], 'file-url-put', 5 * ONE_MINUTE))
        services.append(ServiceDescriptor('TextSummary1', ['file-url'], 'file-url-put', ONE_MINUTE))
        services.append(ServiceDescriptor('WordSenseDisambiguation1', ['file-url'], 'file-url-put', ONE_MINUTE))
        services.append(ServiceDescriptor('VideoSummary1', ['file-url'], 'file-url-put', ONE_MINUTE))
        services.append(ServiceDescriptor('ImageEntityExtraction', ['file-url'], 'file-url-put', ONE_MINUTE))
        services.append(ServiceDescriptor('FacialRecognition', ['file-url'], 'file-url-put', ONE_MINUTE))
        return services
