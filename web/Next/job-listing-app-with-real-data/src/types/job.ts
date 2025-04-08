export interface JobType {
	id: string;
	title: string;
	description: string;
	responsibilities: string;
	requirements: string;
	idealCandidate: string;
	categories: string[];
	opType: string;
	startDate: string;
	endDate: string;
	deadline: string;
	location: string[];
	requiredSkills: string[];
	whenAndWhere: string;
	datePosted: string;
	orgName: string;
	logoUrl: string;

	applicantsCount?: number;
	viewsCount?: number;
	status?: string;
	isBookmarked?: boolean;
	isRolling?: boolean;
}
