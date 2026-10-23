| Component	 |  Value |
|---|---|
| Protocol	|  https |
| Host	  |    api.example.com |
| Path	   |   /students/101 |
| Resource	|  students |
| Resource  |  identifier	101 |

Explanation: The protocol defines how the client communicates with the server. The host identifies the server, while the path identifies the requested resource. In this example, students/101 refers to student record 101.

---------------------------------------------------------------

| Operation	        |      HTTP method	 |   Endpoint |
|---|---|---|
| Retrieve all students	|  GET	      |      /students |
| Create a student	  |    POST	    |      /students |
| Retrieve student 101	|  GET	     |       /students/101 |
| Update student 101	 |   PUT	     |       /students/101 |
| Delete student 101	  |  DELETE	    |     /students/101 |

Different methods communicate the intended action to the API. GET retrieves data, POST creates a resource, PUT updates or replaces it, and DELETE requests its removal.

---------------------------------------------------------------

| Status	|  Meaning	  |    Test |
|---|---|---|
| 200	  |    OK	    |      GET a post; PUT or DELETE a post |
| 201	  |    Created	   |    POST a new post |
| 404	   |   Not Found	  |   GET a nonexistent post |

A successful response means the server processed the request according to its status. A 404 means the server could not find the requested resource.

--------------------------------------------------------------

| Feature	    |    Public API	                    |                Protected API |
|---|---|---|
| Access	   |     May be available without authentication	    |     Requires valid authentication |
| Credentials	   |   Not necessarily required	         |             Often uses an API key or access token |
| Example	   |     JSONPlaceholder posts	             |             A private student management API |
| Security	  |    Access may be unrestricted or rate-limited	  |    Access is controlled by authentication and permissions |

An API being public does not mean every operation is unrestricted.

-------------------------------------------------------------

* Rate limiting restricts how many requests a client can make within a specified period.
* HTTP 429 Too Many Requests indicates that the client has exceeded a rate limit.
* A server may provide a Retry-After header indicating when to try again.
* A robust client should avoid repeatedly retrying immediately. It should wait, apply a sensible retry strategy, and respect server limits.

-------------------------------------------------------------


## Phase 06 — API as an Agent Tool

### Tool Name
Student/Post API Client

### Purpose
Retrieve post information from a REST API and return structured
data that another application or AI agent can use.

### Operations

| Operation | Input | HTTP Method | Endpoint |
|---|---|---|---|
| Get one post | post_id | GET | /posts/{post_id} |
| Get multiple posts | list of post IDs | GET | /posts/{post_id} |
| Get all posts | None | GET | /posts |

### Base URL
https://jsonplaceholder.typicode.com

### Authentication
The demonstration API supports these public GET operations without
a bearer token. The security exercise demonstrates how a protected
API could use an Authorization: Bearer token header.

### Outputs
- A post object containing ID, title, body and user ID.
- A list of retrieved posts for multiple-post operations.
- The total count and first five titles for the complete collection.

### Error Handling
- HTTP 404: requested resource was not found.
- Other HTTP errors: handled using response.raise_for_status().
- Timeout: handled using requests.exceptions.Timeout.
- Network errors: handled using requests.exceptions.RequestException.
- Invalid JSON: handled where JSON parsing is performed.

### Agent Integration
An AI agent could select an appropriate operation, provide the
required input, receive structured JSON data, and use that data
to answer a user's question. Any write or delete operation should
require suitable authorization and safeguards.
