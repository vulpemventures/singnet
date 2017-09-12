#
# services.py - implementation of abstract class defining API for service specs.
#
# Copyright (c) 2017 SingularityNET
#
# Distributed under the MIT software license, see LICENSE file.
#

# Duration constants - durations are in milliseconds
ONE_SECOND = 1000
ONE_MINUTE = 60000
ONE_HOUR = 3600000

class Service():

    def __init__(self, type, input, output, duration):
        self.type = type
        self.input = input
        self.output = output
        self.duration = duration

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __str__(self):
        return "<Service: " + self.type + ", " + self.input + ", " + self.output + \
                ", " + str(self.duration) + ">"

    @classmethod
    def test_services(cls) -> []:
        services = []
        services.append(Service('ImageRecognition1',        'file-url', 'file-url-put', ONE_HOUR))
        services.append(Service('ImageRecognition2',        'file-url', 'file-url-put', ONE_MINUTE))
        services.append(Service('DocumentSummary1',         'file-url', 'file-url-put', 5 * ONE_MINUTE))
        services.append(Service('TextSummary1',             'file-url', 'file-url-put', ONE_MINUTE))
        services.append(Service('WprdSenseDsiambuation1',   'file-url', 'file-url-put', ONE_MINUTE))
        services.append(Service('VideoSummary1',            'file-url', 'file-url-put', ONE_MINUTE))
        services.append(Service('ImageEntityExtraction',    'file-url', 'file-url-put', ONE_MINUTE))
        services.append(Service('FacialRecognition',        'file-url', 'file-url-put', ONE_MINUTE))
        return services
