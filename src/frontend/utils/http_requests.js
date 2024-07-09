// this is an http module



async function post_request(url, response_type, timeout, req_data) {
  return new Promise(function (resolve, reject) {
    console.log(`Starting HTTP POST request to ${url}`);
    let xhr = new XMLHttpRequest();
    xhr.open('POST', url);

    let json = JSON.stringify(req_data);

    xhr.setRequestHeader('Content-type', 'application/json; charset=utf-8');

    xhr.responseType = response_type;
    xhr.timeout = timeout;

    xhr.send(json);

    xhr.onload = function(event) {
      console.log(xhr.getAllResponseHeaders());
      if (this.status >= 200 && this.status < 300) {
        console.log(`Done ${url}, got ${event.total} bytes`);

        resolve(xhr.response);
      } else {
        console.error(`Error: ${xhr.status}: ${xhr.statusText}`);
        reject({
          status: this.status,
          statusText: xhr.statusText
        });
      };
    };

    xhr.ontimeout = function() {
        console.error("Timed out");

        reject({
            status: 408,
            statusText: "Request Timeout"
        });
    };

    xhr.onerror = function() {
        console.error(`Request to ${url} failed -> ${xhr.statusText}`)

        reject({
            status: this.status,
            statusText: xhr.statusText
        });
    };

    xhr.onprogress = function(event) {
        console.log(xhr.readyState);

        if (event.lengthComputable) {
            console.log(`Recieved ${event.loaded} of ${event.total}`);
        } else {
            console.log(`Received ${event.loaded} bytes`);
        };
    };
  });

}


export { post_request };
