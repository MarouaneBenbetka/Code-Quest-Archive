"use client";

import { JobCard } from "./job-card";
import type { JobType } from "@/types/job";
import { useState } from "react";
import { JobSorter } from "./job-sorter";

interface JobListingsProps {
	jobs: JobType[];
}

export default function JobListings({ jobs }: JobListingsProps) {
	const [sortBy, setSortBy] = useState("most-relevant");

	// Sort jobs based on selected option
	const sortedJobs = [...jobs].sort((a, b) => {
		switch (sortBy) {
			case "newest":
				return (
					new Date(b.about.posted_on).getTime() -
					new Date(a.about.posted_on).getTime()
				);
			case "oldest":
				return (
					new Date(a.about.posted_on).getTime() -
					new Date(b.about.posted_on).getTime()
				);
			case "deadline":
				return (
					new Date(a.about.deadline).getTime() -
					new Date(b.about.deadline).getTime()
				);
			default:
				return 0; // most-relevant (default order)
		}
	});

	return (
		<div className="w-full">
			<div className="flex flex-col md:flex-row justify-between items-start md:items-center mb-6">
				<div>
					<h1 className="text-2xl font-bold text-slate-800">
						Opportunities
					</h1>
					<p className="text-sm text-slate-500">
						Showing {jobs.length} results
					</p>
				</div>
				<JobSorter value={sortBy} onChange={setSortBy} />
			</div>

			<div className="grid grid-cols-1 gap-4 max-h-[calc(100vh-150px)] overflow-y-auto">
				{sortedJobs.map((job) => (
					<JobCard key={job.id} job={job} />
				))}
			</div>
		</div>
	);
}
