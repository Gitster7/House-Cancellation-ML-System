# House Cancellation

## ML system available with REST API.

This ML service will use Python 3.11.1 and Django 4.1.6.

<b>This ML system:</b>

<ul>
<li>Can handle many API endpoints.</li>
<li>Each API endpoint can have several ML algorithms with different versions.</li>
<li>ML code and artifacts (files with ML parameters) are stored in the code repository.</li>
<li>Supports fast deployments and continuous integration (tests for both: server and ML code).</li>
<li>Supports monitoring and algorithm diagnostic (support A/B tests).</li>
<li>has a user interface.</li>
</ul>

### Application

<b>Context</b>

The online hotel reservation channels have dramatically changed booking possibilities and customers’ behavior. A significant number of hotel reservations are called-off due to cancellations or no-shows. The typical reasons for cancellations include change of plans, scheduling conflicts, etc. This is often made easier by the option to do so free of charge or preferably at a low cost which is beneficial to hotel guests but it is a less desirable and possibly revenue-diminishing factor for hotels to deal with.

<b>Usage</b>

<em>Predict if the customer is going to honor the reservation or cancel it.</em>

### Data 

<b>The model training file contained the different attributes of customers' reservation details. The detailed data dictionary is given below.</b>

### Data Dictionary

<ul>
<li><b><i>Booking_ID:</i></b> unique identifier of each booking</li>
<li><b><i>no_of_adults:</i></b> Number of adults</li>
<li><b><i>no_of_children:</i></b> Number of Children</li>
<li><b><i>no_of_weekend_nights:</i></b> Number of weekend nights (Saturday or Sunday) the guest stayed or booked to stay at the hotel</li>
<li><b><i>no_of_week_nights:</i></b> Number of week nights (Monday to Friday) the guest stayed or booked to stay at the hotel</li>
<li><b><i>type_of_meal_plan:</i></b> Type of meal plan booked by the customer</li>
<li><b><i>required_car_parking_space:</i></b> Does the customer require a car parking space? (0 - No, 1- Yes)</li>
<li><b><i>room_type_reserved:</i></b> Type of room reserved by the customer. The values are ciphered (encoded) by INN Hotels.</li>
<li><b><i>lead_time:</i></b> Number of days between the date of booking and the arrival date</li>
<li><b><i>arrival_year:</i></b> Year of arrival date</li>
<li><b><i>arrival_month:</i></b> Month of arrival date</li>
<li><b><i>arrival_date:</i></b> Date of the month</li>
<li><b><i>market_segment_type:</i></b> Market segment designation.</li>
<li><b><i>repeated_guest:</i></b> Is the customer a repeated guest? (0 - No, 1- Yes)</li>
<li><b><i>no_of_previous_cancellations:</i></b> Number of previous bookings that were canceled by the customer prior to the current booking</li>
<li><b><i>no_of_previous_bookings_not_canceled:</i></b> Number of previous bookings not canceled by the customer prior to the current booking</li>
<li><b><i>avg_price_per_room:</i></b> Average price per day of the reservation; prices of the rooms are dynamic. (in euros)</li>
<li><b><i>no_of_special_requests:</i></b> Total number of special requests made by the customer (e.g. high floor, view from the room, etc)</li>
<li><b><i>booking_status:</i></b> Flag indicating if the booking was canceled or not.</li>
</ul>

### Screenshots

