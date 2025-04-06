import { JobDetails } from "@/components/main/job-details";
import { jobData } from "@/data/jobs";
import { notFound } from "next/navigation";

export async function generateStaticParams() {
	return jobData.job_postings.map((job) => ({
		id: job.id,
	}));
}

type Params = Promise<{ id: string }>;

export default async function JobPage({ params }: { params: Params }) {
	const jobId = (await params).id;
	const job = jobData.job_postings.find((job) => job.id === jobId);

	if (!job) {
		notFound();
	}

	return (
		<main className="container mx-auto py-3 px-4">
			<JobDetails job={job} />
		</main>
	);
}
