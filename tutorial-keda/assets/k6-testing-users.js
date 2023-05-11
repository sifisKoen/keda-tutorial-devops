import http from 'k6/http';
import { sleep } from 'k6';

// 16 users
// 300 seconds
export let options = {
    vus: 16, 
    duration: '300s', 
};

export default function () {
    http.get('http://<your-service-url>'); // replace with your service URL. We can use the LOOPBACK address:<service-port>
    sleep(1);
}
