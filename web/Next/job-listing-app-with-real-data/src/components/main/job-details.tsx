import type React from "react";
import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import type { JobType } from "@/types/job";
import {
	ArrowLeft,
	Calendar,
	CheckCircle,
	Clock,
	MapPin,
	CircleCheck,
} from "lucide-react";
import Link from "next/link";

interface JobDetailsProps {
	job: JobType;
}

export function JobDetails({ job }: JobDetailsProps) {
	// Parse responsibilities into an array
	const responsibilitiesList = job.responsibilities
		.split("\n")
		.filter((item) => item.trim().length > 0);

	// Format dates for display
	const formattedPostDate = new Date(job.datePosted).toLocaleDateString();
	const formattedDeadline = new Date(job.deadline).toLocaleDateString();
	const formattedStartDate = new Date(job.startDate).toLocaleDateString();
	const formattedEndDate = new Date(job.endDate).toLocaleDateString();

	return (
		<div className="w-full">
			<Button
				variant="ghost"
				asChild
				className="mb-2 pl-0 flex items-center gap-1 w-fit"
			>
				<Link href="/">
					<ArrowLeft className="h-4 w-4" />
					Back to listings
				</Link>
			</Button>

			<Card className="p-6">
				<div className="">
					<h1 className="text-2xl font-bold text-slate-800 mb-1">
						{job.title}
					</h1>
					<p className="text-slate-600">
						{job.orgName} • {job.location.join(", ")}
					</p>
				</div>

				<div className="grid grid-cols-1 md:grid-cols-3 gap-8 mt-6">
					<div className="md:col-span-2 space-y-8">
						<section>
							<h2 className="text-xl font-black text-slate-800 mb-4">
								Description
							</h2>
							<p className="text-slate-700 text-justify">
								{job.description}
							</p>
						</section>

						<section>
							<h2 className="text-xl font-black text-slate-800 mb-4">
								Responsibilities
							</h2>
							<ul className="space-y-2">
								{responsibilitiesList.map(
									(responsibility, index) => (
										<li
											key={index}
											className="flex items-center gap-2"
										>
											<CheckCircle className="h-4 w-4 text-green-500" />
											<span className="text-slate-700">
												{responsibility}
											</span>
										</li>
									)
								)}
							</ul>
						</section>

						<section>
							<h2 className="text-xl font-black text-slate-800 mb-4">
								Ideal Candidate
							</h2>
							<div className="space-y-4">
								<p className="text-slate-700">
									{job.idealCandidate}
								</p>
								<div>
									<h3 className="font-semibold text-slate-800 mb-2">
										Requirements:
									</h3>
									<p className="text-slate-700">
										{job.requirements}
									</p>
								</div>
							</div>
						</section>

						<section>
							<h2 className="text-xl font-black text-slate-800 mb-4">
								When & Where
							</h2>
							<div className="flex items-start gap-2">
								<MapPin className="h-5 w-5 text-blue-500 mt-0.5" />
								<p className="text-slate-700">
									{job.whenAndWhere}
								</p>
							</div>
						</section>
					</div>

					<div className="space-y-8">
						<section className="bg-slate-50 p-4 rounded-lg">
							<h2 className="text-xl font-black text-slate-800 mb-4">
								About
							</h2>
							<div className="space-y-4">
								<InfoItem
									icon={
										<Clock className="h-5 w-5 text-blue-500" />
									}
									label="Posted On"
									value={formattedPostDate}
								/>
								<InfoItem
									icon={
										<Calendar className="h-5 w-5 text-blue-500" />
									}
									label="Deadline"
									value={formattedDeadline}
								/>
								<InfoItem
									icon={
										<MapPin className="h-5 w-5 text-blue-500" />
									}
									label="Location"
									value={job.location.join(", ")}
								/>
								<InfoItem
									icon={
										<Calendar className="h-5 w-5 text-blue-500" />
									}
									label="Start Date"
									value={formattedStartDate}
								/>
								<InfoItem
									icon={
										<Calendar className="h-5 w-5 text-blue-500" />
									}
									label="End Date"
									value={formattedEndDate}
								/>
							</div>
						</section>

						<section>
							<h2 className="text-xl font-black text-slate-800 mb-4">
								Categories
							</h2>
							<div className="flex flex-wrap gap-2">
								{job.categories.map((category, index) => (
									<Badge
										key={index}
										className={`font-semibold ${
											index % 2 === 0
												? "bg-[#EB85331A] text-[#FFB836]"
												: "bg-[#56CDAD1A] text-[#56CDAD]"
										}`}
									>
										{category}
									</Badge>
								))}
							</div>
						</section>

						<section>
							<h2 className="text-xl font-black text-slate-800 mb-4">
								Required Skills
							</h2>
							<div className="flex flex-wrap gap-2">
								{job.requiredSkills.map((skill, index) => (
									<Badge
										key={index}
										className="bg-blue-50 text-blue-700 border-blue-200"
									>
										{skill}
									</Badge>
								))}
							</div>
						</section>
					</div>
				</div>
			</Card>
		</div>
	);
}

function InfoItem({
	icon,
	label,
	value,
}: {
	icon: React.ReactNode;
	label: string;
	value: string;
}) {
	return (
		<div className="flex items-start gap-3">
			<div className="mt-1 border rounded-full border-[#D6DDEB] p-1">
				{icon}
			</div>
			<div>
				<p className="text-sm text-slate-500">{label}</p>
				<p className="font-medium text-slate-800">{value}</p>
			</div>
		</div>
	);
}

function Badge({
	children,
	className,
}: {
	children: React.ReactNode;
	className?: string;
}) {
	return (
		<span
			className={`inline-flex items-center px-2.5 py-1 rounded-full text-xs font-medium ${className}`}
		>
			{children}
		</span>
	);
}
