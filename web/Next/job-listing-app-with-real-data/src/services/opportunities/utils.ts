import { fetchOpportunities, fetchOpportunityById } from "./client";

export const getOpportunitiesQueryOptions = (params: any) => {
	return {
		queryKey: ["opportunities"],
		queryFn: async () => fetchOpportunities(params),
	};
};

export const getOpportynityByIdQueryOptions = (id: string) => {
	return {
		queryKey: ["opportunity", id],
		queryFn: async () => fetchOpportunityById(id),
		enabled: !!id,
	};
};
