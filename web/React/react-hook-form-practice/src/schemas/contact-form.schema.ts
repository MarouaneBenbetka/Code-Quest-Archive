import { z } from "zod";

export const contactFormSchema = z.object({
	userName: z
		.string()
		.min(3, "Username must be at least 3 characters long")
		.max(20, "Username must be at most 20 characters long")
		.regex(/^[A-Za-z ]+$/i, "Username must contain only letters"),
	email: z
		.string()
		.min(1, "This field is required")
		.email("Invalid email address"),

	message: z.string().min(6, "Message must be at least 6 characters long"),
});
export type ContactFormValues = z.infer<typeof contactFormSchema>;
