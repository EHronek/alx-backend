#!/usr/bin/yarn dev

import { createClient } from "redis";
const client = createClient();

client.on('error', (error) => {
  console.log(` Redis client not connected to the server: ${error.toString()}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});
