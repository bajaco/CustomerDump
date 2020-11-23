# Customer Dump

This collects environment data, along with Python and Ubuntu packages and outputs a JSON file.

The idea is that eventually this outputs a POST request to a Flask or Django backend, which adds the submission to a ticketing database.


### Next steps

- Implement backend.
- Change JSON file dump to post request to backend.
- Implement other routes in backend for queries.
- Frontend in React or similar with ajax filtering to find conflicting packages.
