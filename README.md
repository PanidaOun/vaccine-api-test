# test-project-API-endpoint
* Project: Flamby
* Endpoint: Get reservation by ID.\
Test feature about get reservation by ID.

| ID | Name of Test Case | Description | Result | 
| :---:         |     :---     | :---| :---: |
| 1   | test_get_reservation_by_ID()| Test if user can get reservation by input specific ID.|  Pass|
| 2   | test_get_reservation_by_ID_using_uncorrect_link()| Test if user can get reservation by input uncorrect link.|  Pass|
| 3   | test_get_reservation_by_ID_check_content_type_equals_jso()| Test when user get reservation by input specific ID and the outcome is json format.|  Pass|
| 4   | test_get_reservation_by_ID_equals_specific_ID()| Test when user get reservation by input specific ID and the outcome is the correct reservation.|  Pass|
| 5   | test_get_unvalid_reservation_by_ID()| Test when user get reservation by input unvalid ID.|  Pass|
| 6   | test_get_unvalid_reservation_by_ID_given_message_error()| Test when user get reservation by input unvalid ID and the outcome is the message error.|  Pass|
| 7   | test_headers_server()| Test the headers of server when get reservation.|  Pass|


