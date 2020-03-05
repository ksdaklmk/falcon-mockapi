import http from 'k6/http';

export default function () {
    var url = 'https://sandbox.api.krungsri.net/ndid/utility/sign';
    var payload = JSON.stringify({
        email: 'johndoe@example.com',
        password: 'PASSWORD'
    });

    var params = {
        headers: {
            'Content-Type': 'application/json',
            'API-Key': '',
            'X-Transaction-ID': '',
            'X-Transaction-DateTime': ''
        },
    };

    http.post(url, payload, params);
}