"use client";
import JobListings from "@/components/main/job-listings";
import { useOpportunitiesQuery } from "@/services/opportunities/queries";
import Loading from "./loading";

const PageClient = () => {
	const { data, isLoading, isError } = useOpportunitiesQuery({});
	if (isLoading) {
		return <Loading />;
	}

	if (isError) {
		throw new Error("Error loading opportunities");
	}

	return (
		<main className="container mx-auto py-8 px-4 max-w-[900px]">
			<JobListings jobs={data.data} />
		</main>
	);
};

export default PageClient;
