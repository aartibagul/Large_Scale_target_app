# Metrix and Target_app
#### 
Metrix is an app that allows you to initialize Counters and increment them. It can be found in the metrix/ folder. After importing the counters file from metrix, you can initialize new counters as `c = Counters("app_name", "counter_name")` You can then increment these counters when needed using increment() and increment_by() methods. Eg; `c.increment()` or ` c.increment_by(5)` .Sample code can also be found in testing.py. The app creates files in /tmp/ folder to store the values of the counters.
It also has a views.py file that displays these counters with a <url_of_server>\metrix url which are then scraped by a [monitoring app](https://github.com/aartibagul/monitoring_app) and displayed on a dashboard.

You must include  url(r'^metrix/', include('metrix.urls')) in the urls.py file of the project (in this case "test/urls.py") and add 'metrix' in the installed apps section of settings.py of the project (in this case "test/settings.py").

#### testing.py
testing.py initializes two Counters from the metrix app and increments their values. As the name suggests, this is used for testing purposes.


#### Future work
Currently, the counters are stored in files in the \tmp\ folder. We could store the counters in a database or store it in local memory. \\
We could package the metrix app to make it re-usable and allow other apps to import the app. Currently, you have to copy the metrix folder into your project to be able to use it.
