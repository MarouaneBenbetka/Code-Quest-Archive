import { useQuery } from "@tanstack/react-query";
import {
	getOpportunitiesQueryOptions,
	getOpportynityByIdQueryOptions,
} from "./utils";

export const useOpportunitiesQuery = (params: any) => {
	return useQuery({ ...getOpportunitiesQueryOptions(params) });
};

export const useOpportunityByIdQuery = (id: string) => {
	return useQuery({ ...getOpportynityByIdQueryOptions(id) });
};
