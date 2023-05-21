import http from 'k6/http';
import { sleep } from 'k6';

export let options = {
  vus: 16,
  duration: '300s',
};

export default function () {
  http.get('http://172.30.1.2:31386/get_url'); // replace with your service URL. We can use the LOOPBACK address:<service-port>
  sleep(1);
}