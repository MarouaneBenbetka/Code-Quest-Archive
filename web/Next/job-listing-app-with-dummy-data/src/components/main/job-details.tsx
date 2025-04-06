import type React from "react";
import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import type { JobType } from "@/types/job";
import {
	ArrowLeft,
	Calendar,
	CheckCheckIcon,
	CheckIcon,
	CircleCheckBig,
	Clock,
	MapPin,
} from "lucide-react";
import Link from "next/link";

interface JobDetailsProps {
	job: JobType;
}

export function JobDetails({ job }: JobDetailsProps) {
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
						{job.company} • {job.about.location}
					</p>
				</div>

				<div className="grid grid-cols-1 md:grid-cols-3 gap-8">
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
								{job.responsibilities.map(
									(responsibility, index) => (
										<li
											key={index}
											className="flex items-center gap-2"
										>
											<CircleCheckBig className=" h-3 w-3 text-green-500 " />
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
								Ideal Candidate we want
							</h2>
							<ul className="space-y-4 list-disc pl-5">
								<li>
									<span className="font-semibold">
										Young({job.ideal_candidate.age} year
										old) {job.ideal_candidate.gender}
									</span>{" "}
									{job.title.toLowerCase()}
								</li>
								{job.ideal_candidate.traits.map(
									(trait, index) => {
										const [title, description] =
											trait.split(":");
										return (
											<li key={index}>
												<span className="font-semibold">
													{title}:
												</span>{" "}
												{description}
											</li>
										);
									}
								)}
							</ul>
						</section>

						<section>
							<h2 className="text-xl font-black text-slate-800 mb-4">
								When & Where
							</h2>
							<div className="flex items-start gap-2">
								<Calendar className="h-5 w-5 text-blue-500 mt-0.5" />
								<p className="text-slate-700">
									{job.when_where}
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
									value={job.about.posted_on}
								/>
								<InfoItem
									icon={
										<Calendar className="h-5 w-5 text-blue-500" />
									}
									label="Deadline"
									value={job.about.deadline}
								/>
								<InfoItem
									icon={
										<MapPin className="h-5 w-5 text-blue-500" />
									}
									label="Location"
									value={job.about.location}
								/>
								<InfoItem
									icon={
										<Calendar className="h-5 w-5 text-blue-500" />
									}
									label="Start Date"
									value={job.about.start_date}
								/>
								<InfoItem
									icon={
										<Calendar className="h-5 w-5 text-blue-500" />
									}
									label="End Date"
									value={job.about.end_date}
								/>
							</div>
						</section>

						<section>
							<h2 className="text-xl font-black text-slate-800 mb-4">
								Categories
							</h2>
							<div className="flex flex-wrap gap-2">
								{job.about.categories.map((category, index) => (
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
								{job.about.required_skills.map(
									(skill, index) => (
										<Badge
											key={index}
											className="bg-blue-50 text-blue-700 border-blue-200"
										>
											{skill}
										</Badge>
									)
								)}
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
