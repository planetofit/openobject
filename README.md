# openobject
A python object to rotate api calls between application and networking devices

Python main() calls an objectclass to capture the embeded build number for ci/cds to pass the build number to sre
SRE spits the data in telemetry calls
Telemetry calls are pulled from api and passed to the next build number

Python save this transactions in its default cache folder which can be a single file in structured language such as json and xml
Cache file act as a default to maintain and file and folder structure for such transaction

Goal of this object is to capture exchnage calls between apis so active and passive port calls are rotated


Example:
url1: url1.call > spits a value from embedded in api header
url2: url2.call > capture the output of url1 and send a post call to url4
url3: url3.call > perform get/set function in a loop by using a loopback call to url4
url4: a loopback url, acting as an agent to call itself to 127.0.0.1

End result:
From git commit id of the developer to sre's build number a single transaction is maintained for ci/cd agents
