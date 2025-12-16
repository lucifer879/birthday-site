import { useUserUpdateRequest } from '@dynamic-labs/sdk-react-core';

export function UpdateEmail() {
  const { updateUser } = useUserUpdateRequest();

  const onSubmit = async (e) => {
    e.preventDefault();
    const email = e.currentTarget.email.value;
    const { isEmailVerificationRequired, verifyOtp } = await updateUser({ email });

    if (isEmailVerificationRequired) {
      const token = window.prompt('Enter the 6-digit code sent to your email');
      await verifyOtp(token!);
    }
  };

  return (
    <form onSubmit={onSubmit}>
      <input type="email" name="email" placeholder="Email" />
      <button type="submit">Save</button>
    </form>
  );
}