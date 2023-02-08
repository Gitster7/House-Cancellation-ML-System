import inspect
from .registry import MLRegistry
from django.test import TestCase
from .cancel_classifier import Classifier

class MLTests(TestCase):
    def test_classifier(self):
        input_data = {
            "Booking_ID":"INN00001",
            "no_of_adults":2,
            "no_of_children":0,
            "no_of_weekend_nights":1,
            "no_of_week_nights":2,
            "type_of_meal_plan":"Meal Plan 1",
            "required_car_parking_space":0,
            "room_type_reserved":"Room_Type 1",
            "lead_time":224,
            "arrival_year":2017,
            "arrival_month":10,
            "arrival_date":2,
            "market_segment_type":"Offline",
            "repeated_guest":0,
            "no_of_previous_cancellations":0,
            "no_of_previous_bookings_not_canceled":0,
            "avg_price_per_room":65.0,
            "no_of_special_requests":0,
        }

        cls = Classifier()
        response = cls.compute_prediction(input_data)
        self.assertEqual('OK', response['status'])
        self.assertTrue('label' in response)
        self.assertEqual('Not Cancel', response['label'])

    def test_registry(self):
        registry = MLRegistry()
        self.assertEqual(len(registry.endpoints), 0)
        endpoint_name = "cancel_classifier"
        algorithm_object = Classifier()
        algorithm_name = "random forest"
        algorithm_status = "production"
        algorithm_version = "0.0.1"
        algorithm_owner = "Omkar Vatsa"
        algorithm_description = "Random Forest with simple pre- and post-processing"
        algorithm_code = inspect.getsource(Classifier)
        # add to registry
        registry.add_algorithm(endpoint_name, algorithm_object, algorithm_name,
                    algorithm_status, algorithm_version, algorithm_owner,
                    algorithm_description, algorithm_code)
        # there should be one endpoint available
        self.assertEqual(len(registry.endpoints), 1)
