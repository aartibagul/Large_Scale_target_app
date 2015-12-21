# Metrix and Target_app
#### 
Metrix is an app that allows you to initialize Counters objects by specifying an app_name and a counter_name. You can then increment these counters when needed using increment() and increment_by() methods. Sample code can be found in testing.py. It also has a views.py file that displays these counters which are then scraped by a [monitoring app](https://github.com/aartibagul/monitoring_app) and displayed on a dashboard.

The app creates files in /tmp/ folder to store the values of the counters.

You must include  url(r'^metrix/', include('metrix.urls')) in the urls.py file of the project (in this case "test/urls.py").

#### testing.py
testing.py initializes two Counters from the metrix app and increments their values. As the name suggests, this is used for testing purposes.
