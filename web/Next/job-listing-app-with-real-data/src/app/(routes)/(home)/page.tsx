import JobListings from "@/components/main/job-listings";
import { jobData } from "@/data/jobs";
import { useServerData } from "@/hooks/use-server-data";
import { getOpportunitiesQueryOptions } from "@/services/opportunities/utils";
import PageClient from "./page-client";

export default async function Home() {
	const { ServerData } = await useServerData([
		getOpportunitiesQueryOptions({}),
	]);

	return (
		<ServerData>
			<PageClient />
		</ServerData>
	);
}
