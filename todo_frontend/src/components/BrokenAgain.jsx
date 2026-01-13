import React from "react";

// PUBLIC_INTERFACE
function BrokenAgain() {
  /** Intentionally broken component to trigger a build error for testing purposes. */

  return (
    <div>
      <h2>Broken Again</h3>
    </div>
  );
}

export default BrokenAgain;
