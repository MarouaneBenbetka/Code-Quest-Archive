"use client";

import { JobDetails } from "@/components/main/job-details";
import { useOpportunityByIdQuery } from "@/services/opportunities/queries";
import NotFound from "./not-found";
import Loading from "./loading";

const PageClient = ({ jobId }: { jobId: string }) => {
	const { data, isLoading, isError } = useOpportunityByIdQuery(jobId);

	if (isLoading) return <Loading />;

	if (isError) throw new Error("Error loading opportunity details");

	const job = data.data;

	if (!job) {
		return NotFound();
	}
	return (
		<main className="container mx-auto py-3 px-4">
			<JobDetails job={data.data} />
		</main>
	);
};

export default PageClient;
