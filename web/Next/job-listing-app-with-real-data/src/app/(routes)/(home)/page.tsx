import JobListings from "@/components/main/job-listings";
import { jobData } from "@/data/jobs";

export default function Home() {
	return (
		<main className="container mx-auto py-8 px-4 max-w-[900px]">
			<JobListings jobs={jobData.job_postings} />
		</main>
	);
}
