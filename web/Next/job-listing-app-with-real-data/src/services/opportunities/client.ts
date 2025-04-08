"use server";

import { API_ROUTES } from "../api/api-routes";
import { apiClient } from "../api/client";

export const fetchOpportunities = async (body: any) => {
	const { data } = await apiClient.get(`${API_ROUTES.opprotunities}/search`, {
		params: body,
	});

	return data;
};

export const fetchOpportunityById = async (id: string) => {
	const { data } = await apiClient.get(`${API_ROUTES.opprotunities}/${id}`);
	return data;
};
