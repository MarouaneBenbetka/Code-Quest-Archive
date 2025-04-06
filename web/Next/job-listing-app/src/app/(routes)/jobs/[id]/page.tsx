import { JobDetails } from "@/components/main/job-details";
import { jobData } from "@/data/jobs";
import { notFound } from "next/navigation";

export async function generateStaticParams() {
	return jobData.job_postings.map((job) => ({
		id: job.id,
	}));
}

interface JobPageProps {
	params: {
		id: string;
	};
}

export default function JobPage({ params }: JobPageProps) {
	// Simulate a network request
	const job = jobData.job_postings.find((job) => job.id === params.id);

	// If job not found, show 404 page
	if (!job) {
		notFound();
	}

	return (
		<main className="container mx-auto py-3 px-4">
			<JobDetails job={job} />
		</main>
	);
}
