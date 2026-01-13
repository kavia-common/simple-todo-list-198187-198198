import React from "react";

// PUBLIC_INTERFACE
function BrokenComponent() {
  /** Intentionally broken component to trigger a build error for testing. */

  return (
    <div>
      <h2>Build Error Test</h2>
    </div>
  );
}

export default BrokenComponent;
