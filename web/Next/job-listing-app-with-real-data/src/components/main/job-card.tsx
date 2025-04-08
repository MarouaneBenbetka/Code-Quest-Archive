import type React from "react";
import { Avatar } from "@/components/ui/avatar";
import { Card } from "@/components/ui/card";
import type { JobType } from "@/types/job";
import Link from "next/link";
import { AvatarFallback, AvatarImage } from "@radix-ui/react-avatar";
import { cn } from "@/lib/utils";

interface JobCardProps {
	job: JobType;
}

export function JobCard({ job }: JobCardProps) {
	return (
		<Link href={`/jobs/${job.id}`} className="block">
			<Card className="w-full p-4 hover:shadow-md transition-shadow cursor-pointer">
				<div className="flex gap-4">
					<Avatar className="h-16 w-16 rounded-full bg-blue-300 flex items-center justify-center overflow-hidden">
						<AvatarImage
							src={job.logoUrl}
							alt={job.title}
							className="h-full w-full object-cover"
						/>
						<AvatarFallback className="text-blue-600">
							{job.title.substring(0, 2).toUpperCase()}
						</AvatarFallback>
					</Avatar>

					<div className="flex-1">
						<h3 className="font-semibold text-slate-800">
							{job.title}
						</h3>
						<p className="text-sm text-slate-600">
							{job.orgName} • {job.location.join(", ")}
						</p>

						<p className="text-sm mt-2 text-slate-700 line-clamp-2">
							{job.description}
						</p>

						<div className="flex flex-wrap gap-2 mt-3">
							<Badge
								variant="outline"
								className="bg-[#56CDAD1A] text-[#56CDAD] font-semibold"
							>
								{job.opType === "inPerson"
									? "In Person"
									: "Virtual"}
							</Badge>
							{job.categories
								.slice(0, 2)
								.map((category, index) => (
									<Badge
										key={index}
										variant="outline"
										className={cn(
											"font-semibold border",
											index % 2 === 0
												? "text-[#FFB836] border-[#FFB836]"
												: "text-[#4640DE] border-[#4640DE]",
											"px-2"
										)}
									>
										{category}
									</Badge>
								))}
						</div>
					</div>
				</div>
			</Card>
		</Link>
	);
}

function Badge({
	children,
	className,
	variant = "default",
}: {
	children: React.ReactNode;
	className?: string;
	variant?: "default" | "outline";
}) {
	return (
		<span
			className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium ${className}`}
		>
			{children}
		</span>
	);
}
