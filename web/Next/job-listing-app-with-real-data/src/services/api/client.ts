"use server";

import axios from "axios";

const BASE_URL = process.env.API_BASE_URL;

export const apiClient = axios.create({
	baseURL: BASE_URL,
});
