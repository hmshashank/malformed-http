Sample python-app which returns malformed responses on hitting certain endpoints

-->  Response for '/' which provides Instructions:
```
"Test app to produce good and bad responses\n"
"For successful 404 response, use /good URL\n"
"For incorrectly formatted response, use /bad URL\n".encode("utf-8"))
```
--> Response for '/good' (Good endpoint):
```
HTTP/1.1 404 Not Found
Date: Fri, 05 May 2023 07:41:22 GMT
Server: Apache/2.4.53 (Unix) OpenSSL/3.0.7+akamai
Transfer-Encoding: chunked

This is the good page.
```

--> Respose for '/bad' (Malformed endpoint):
```
HTTP/1.1 200 OK
Date: Fri, 14 Apr 2023 05:15:17 GMT
Server: Apache/2.4.53 (Unix) OpenSSL/3.0.7+akamai
Transfer-Encoding: chunked

HTTP/1.0 b'404 Not Found'
This is the bad page.
```%
