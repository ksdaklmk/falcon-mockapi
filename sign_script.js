import "./libs/shim/core.js";

export let options = { maxRedirects: 4 };

const Request = Symbol.for("request");
postman[Symbol.for("initial")]({
  options
});

export default function() {
  postman[Request]({
    name: "Sign UAT",
    id: "66edffec-bc75-4581-a06c-eea38728a7f1",
    method: "POST",
    address: "https://sandbox.api.krungsri.net/native/ndid/eSignature/sign",
    data:
      '{\r\n\t"payload": {\r\n\t\t"identifier": "3101800885320",\r\n\t\t"object_type": "01",\r\n\t\t"kid": "a3gyMDE4MTIyNjE2MjgxODgyNTRlOTY4NTJmYzQ3Y2RhNTMwNWE2Yzc5NDM2ODIybg==",\r\n\t\t"domain": "MIRAI",\r\n\t\t"namespace": "citizen_id",\r\n\t\t"request_id": "20200113112054117608",\r\n\t\t"reference_number": "x2020011311015301aabd27eaa44ae99590599257c88979",\r\n\t\t"object": "JVBERi0xLjUKJeLjz9MKNCAwIGVFT0YK"\r\n\t},\r\n\t"header": {\r\n\t\t"channel_id": "MIRAI"\r\n\t}\r\n}\r\n',
    headers: {
      "API-Key": "l71ad26790bd0f4b9d81b215670b54fb3e",
      "X-Client-Transaction-DateTime": "2020-01-13T11:01:00.449+07:00",
      "X-Client-Transaction-ID": "a01fa0ae-190a-49d5-9cc1-465f9f9ab0dc",
      "Content-Type": "application/json"
    }
  });
}
