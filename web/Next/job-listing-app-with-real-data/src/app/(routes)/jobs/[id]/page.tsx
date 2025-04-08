import { JobDetails } from "@/components/main/job-details";
import { jobData } from "@/data/jobs";
import { useServerData } from "@/hooks/use-server-data";
import { getOpportynityByIdQueryOptions } from "@/services/opportunities/utils";
import { notFound } from "next/navigation";
import PageClient from "./page-client";

export async function generateStaticParams() {
	return jobData.job_postings.map((job) => ({
		id: job.id,
	}));
}

type Params = Promise<{ id: string }>;

export default async function JobPage({ params }: { params: Params }) {
	const jobId = (await params).id;

	const { ServerData } = await useServerData([
		getOpportynityByIdQueryOptions(jobId),
	]);

	return (
		<ServerData>
			<PageClient jobId={jobId} />
		</ServerData>
	);
}
