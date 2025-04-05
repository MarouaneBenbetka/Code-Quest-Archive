import { useForm } from "react-hook-form";
import { useState } from "react";

import { zodResolver } from "@hookform/resolvers/zod";
import {
	contactFormSchema,
	ContactFormValues,
} from "../schemas/contact-form.schema";
import styles from "../styles/contact-form.module.css";

const ContactForm = () => {
	const [showPopup, setShowPopup] = useState(false);
	const [submittedData, setSubmittedData] =
		useState<ContactFormValues | null>(null);

	const {
		register,
		handleSubmit,
		reset,
		formState: { errors, isSubmitting },
	} = useForm<ContactFormValues>({
		resolver: zodResolver(contactFormSchema),
		defaultValues: {
			userName: "",
			email: "",
			message: "",
		},
	});

	const onSubmit = (data: ContactFormValues) => {
		// Simulate API call
		return new Promise<void>((resolve) => {
			setTimeout(() => {
				console.log(data);
				setSubmittedData(data);
				setShowPopup(true);
				reset();
				resolve();
			}, 1000);
		});
	};

	const closePopup = () => {
		setShowPopup(false);
	};

	return (
		<div className={styles.pageContainer}>
			<div className={styles.formContainer}>
				<div className={styles.formHeader}>
					<h1 className={styles.mainTitle}>Get in Touch</h1>
					<p className={styles.subtitle}>
						We'd love to hear from you! Fill out the form below.
					</p>
				</div>

				<form
					onSubmit={handleSubmit(onSubmit)}
					noValidate
					className={styles.form}
				>
					<div className={styles.formSection}>
						<div className={styles.formControl}>
							<label htmlFor="userName" className={styles.label}>
								Name <span className={styles.required}>*</span>
							</label>
							<input
								type="text"
								id="userName"
								className={`${styles.input} ${
									errors.userName ? styles.inputError : ""
								}`}
								placeholder="Enter your name"
								{...register("userName")}
							/>
							{errors.userName && (
								<p className={styles.error}>
									{errors.userName.message}
								</p>
							)}
						</div>

						<div className={styles.formControl}>
							<label htmlFor="email" className={styles.label}>
								Email <span className={styles.required}>*</span>
							</label>
							<input
								type="email"
								id="email"
								className={`${styles.input} ${
									errors.email ? styles.inputError : ""
								}`}
								placeholder="your.email@example.com"
								{...register("email")}
							/>
							{errors.email && (
								<p className={styles.error}>
									{errors.email.message}
								</p>
							)}
						</div>

						<div className={styles.formControl}>
							<label htmlFor="message" className={styles.label}>
								Message{" "}
								<span className={styles.required}>*</span>
							</label>
							<textarea
								id="message"
								className={`${styles.textarea} ${
									errors.message ? styles.inputError : ""
								}`}
								placeholder="Tell us what's on your mind..."
								{...register("message")}
							></textarea>
							{errors.message && (
								<p className={styles.error}>
									{errors.message.message}
								</p>
							)}
						</div>
					</div>

					<div className={styles.formFooter}>
						<button
							type="submit"
							className={styles.button}
							disabled={isSubmitting}
						>
							{isSubmitting ? "Sending..." : "Send Message"}
						</button>
					</div>
				</form>
			</div>

			{showPopup && submittedData && (
				<div className={styles.popupOverlay}>
					<div className={styles.popup}>
						<div className={styles.popupHeader}>
							<h2>Message Sent!</h2>
							<button
								onClick={closePopup}
								className={styles.closeButton}
							>
								×
							</button>
						</div>
						<div className={styles.popupContent}>
							<div className={styles.successIcon}>✓</div>
							<p>
								Thank you for reaching out,{" "}
								<strong>{submittedData.userName}</strong>!
							</p>
							<p>
								We've received your message and will respond to{" "}
								<strong>{submittedData.email}</strong> shortly.
							</p>
						</div>
						<div className={styles.popupFooter}>
							<button
								onClick={closePopup}
								className={styles.popupButton}
							>
								Close
							</button>
						</div>
					</div>
				</div>
			)}
		</div>
	);
};

export default ContactForm;
